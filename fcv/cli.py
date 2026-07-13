import click
import sys
from typing import List

from fcv.parsers.fortran_parser import parse_fortran_file
from fcv.parsers.c_parser import parse_c_header
from fcv.engine.comparator import compare_interfaces, Mismatch
from fcv.engine.abi import run_abi_checks
from fcv.report.formatter import ReportFormatter

@click.group()
def cli():
    """Fortran-C Cross-Language Interface Validator"""
    pass

@cli.command()
@click.argument('fortran_file', type=click.Path(exists=True))
@click.argument('c_header', type=click.Path(exists=True))
@click.option('--format', type=click.Choice(['text', 'json', 'sarif']), default='text', help='Output format')
@click.option('--severity', type=click.Choice(['error', 'warning', 'info']), default='warning', help='Minimum severity to report')
@click.option('--platform', type=click.Choice(['lp64', 'ilp64', 'llp64']), default='lp64', help='Integer size model')
@click.option('--use-flang', is_flag=True, help='Use Flang for parsing')
@click.option('--no-color', is_flag=True, help='Disable terminal colors')
@click.option('--cflags', default='', help='Additional C compiler preprocessor flags (e.g. -I/path -DNAME)')
@click.option('--c-prefix', default='', help='C function prefix')
@click.option('--c-suffix', default='', help='C function suffix')
@click.option('--f-prefix', default='', help='Fortran function prefix')
@click.option('--f-suffix', default='', help='Fortran function suffix')
@click.option('--name-map', default='', help='Comma-separated name mapping in format key=value,key2=value2')
def validate(fortran_file, c_header, format, severity, platform, use_flang, no_color, cflags, c_prefix, c_suffix, f_prefix, f_suffix, name_map):
    """Validate a Fortran interface against a C header."""
    import shlex
    cflags_list = shlex.split(cflags) if cflags else None
    
    name_map_dict = {}
    if name_map:
        for pair in name_map.split(','):
            if '=' in pair:
                k, v = pair.split('=', 1)
                name_map_dict[k.strip().lower()] = v.strip()
                
    from fcv.parsers.flang_parser import parse_fortran_file_flang, fortran_parser_backend_name
    if format == 'text':
        click.echo(f"INFO: Using Fortran frontend: {fortran_parser_backend_name()}", err=True)
        
    if use_flang:
        f_procs = parse_fortran_file_flang(fortran_file, platform, raise_on_error=True)
    else:
        f_procs = parse_fortran_file_flang(fortran_file, platform, raise_on_error=False)
    c_procs = parse_c_header(c_header, platform, cflags=cflags_list)
    
    mismatches = compare_interfaces(f_procs, c_procs, platform,
                                    name_map=name_map_dict,
                                    c_prefix=c_prefix, c_suffix=c_suffix,
                                    f_prefix=f_prefix, f_suffix=f_suffix)
    mismatches = run_abi_checks(f_procs, c_procs, mismatches)
    
    # Filter by severity
    sev_levels = {"info": 1, "warning": 2, "error": 3}
    min_sev = sev_levels[severity]
    
    filtered = []
    for m in mismatches:
        m_sev = sev_levels.get(m.severity.lower(), 1)
        if m_sev >= min_sev:
            filtered.append(m)
            
    formatter = ReportFormatter(use_color=not no_color)
    
    if format == 'text':
        formatter.format_text(filtered)
    elif format == 'json':
        print(formatter.format_json(filtered))
    elif format == 'sarif':
        print(formatter.format_sarif(filtered))
        
    if any(m.severity == "ERROR" for m in filtered):
        sys.exit(1)
    sys.exit(0)

@cli.command()
def version():
    """Show version info"""
    click.echo("fcvalidator v0.1.0")

if __name__ == '__main__':
    cli()
