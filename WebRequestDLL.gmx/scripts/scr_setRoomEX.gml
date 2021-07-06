///scr_setRoomEX(json)
// This will set the room environment variables

var map = argument0;
var _map = map[?"room"]

obj_main.EX_room_width = _map[?"width"];
obj_main.EX_room_height = _map[?"height"];
obj_main.EX_room_speed = _map[?"speed"];
