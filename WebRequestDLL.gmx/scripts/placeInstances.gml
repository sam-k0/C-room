/// placeInstances(jmap)

var jmap = argument0;

var rmap = jmap[?"room"];
var instances = rmap[?"instances"];
var instlist = instances[?"instance"];

show_debug_message(string(ds_list_size(instlist)))

for(i = 0; i<ds_list_size(instlist); i++)
{
    var instmap = instlist[|i]
    var newinst = instance_create(int64(instmap[?"@x"]),int64(instmap[?"@y"]),obj_instance);
    
    newinst.EX_obj_name = instmap[?"@objName"]
    newinst.EX_name = instmap[?"@name"]
    newinst.EX_code = instmap[?"@code"]
    newinst.EX_locked = instmap[?"@locked"]
    newinst.EX_scaleX = instmap[?"@scaleX"]
    newinst.EX_scaleY = instmap[?"@scaleX"]
    newinst.EX_color = instmap[?"@colour"]
    newinst.EX_rotation = int64(instmap[?"@rotation"])
    
    
}


