///scr_drawTextOutlined(font,color,thiccness,text,x,y)

_font = argument0;
_col = argument1;
_thiccness = argument2;
txt = argument3;
_x = argument4;
_y = argument5;

var oldCol = draw_get_color();
draw_set_font(_font);
// draw bg
draw_set_color(c_black)
draw_text(_x-_thiccness,_y,txt);
draw_text(_x+_thiccness,_y,txt);
draw_text(_x,_y+_thiccness,txt);
draw_text(_x,_y-_thiccness,txt);
// draw colored
draw_set_color(_col);
draw_text(_x,_y,txt)
draw_set_color(oldCol);

