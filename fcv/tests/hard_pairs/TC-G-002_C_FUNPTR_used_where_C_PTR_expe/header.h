/* header.h */
typedef void (*event_handler)(int event_id);
void store_handler(event_handler handler);