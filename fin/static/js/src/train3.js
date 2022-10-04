//TODO: move bubbles and arcs into sep class and export using require, module.export
import p5 from "./p5";
import {Bubble} from './bubble';
import {Arc, ChoosableArc} from './arc';
import *  as c from './constants';
import myjspsych from "./myjspsych";
import jspsych from "./jspsych";

const myJsPsynchEvents = myjspsych({setup: '0x378', trigger: 1});

let bubble,
    game,
    arcs = [];
let chosen_arc_id=0;
let fin=0;
let countwin=9;
let timerestout=timerestin;
var tmp = document.getElementById('tmp');
console.log(timerestin);
var currentTime=0;
var currentTime2=0;


window.onload=function () {currentTime= new Date(); }

function mf(){ currentTime2= new Date();
timerestout=timerestin-Math.floor(currentTime2-currentTime);
$('#timerest').val(timerestout);
//tmp = document.getElementById('tmp');
console.log(timerestout);
//tmp.innerHTML =timerestout;

}


                setTimeout(function () {mf(this);
console.log('timerestin>>');console.log(timerestin);
                    $('form#form').submit();
                }, timerestin);

const s = (p) => {
    let chosen_arc;
    p.setup = function () {
        p.createCanvas(c.canv_size, c.canv_size);
        bubble = new Bubble(p);
        c.arc_lengths.forEach((i, j) => {
            let start_angle = j === 0 ? 0 : arcs[j - 1].uncorrected_angles.end;
            let end_angle = start_angle + i;
            let color = c.colors[j];
            let A = choose_difficulty === true ? ChoosableArc : Arc;
            let t = new A({
                p: p,
                end_angle: end_angle,
                col: color,
                chosen: false,
                start_angle: start_angle,
                id: j,
                transparency: 255,
            });
            arcs.push(t);
        });
    };

    p.draw = function () {
        p.background('green');
        p.stroke(1);
        p.strokeWeight(1);
        p.noFill();
        p.ellipse(c.centerX, c.centerY, c.diameter);
        bubble.display();
        arcs.forEach((i, j) => {
            i.display();
        })

    };
    let event_happened = () => {
//       console.log('evhappen')
    if (typeof chosen_arc_id =='undefined') {chosen_arc_id=0; }
    let old_chosen_arc_id=chosen_arc_id;
    let in_canvas = (p.mouseX > 0 && p.mouseX < c.canv_size && p.mouseY > 0 && p.mouseY < c.canv_size);
    if (fin<2) {
    if (in_canvas) {
console.log('in__canvas_');
//            if (choose_difficulty === true) {
                arcs.forEach((i, j) => {
                    if (i.is_clicked()) {
                        arcs.forEach((l, m) => {
                            l.chosen = false
                        });
			fin=1;
                        i.chosen = true;
                        i.do_if_clicked();
                        chosen_arc_id=i.id;
			choose_difficulty=false;
                    }
                });
                
if (fin==0){
console.log('not__arc');
            chosen_arc=arcs[chosen_arc_id];
            chosen_arc.chosen=true;
            arcs.forEach(l => l.set_transparency(80));
            let old_speed = speed;
            speed = 0;
            fin=2;
            let vv=bubble.is_within_arc(chosen_arc);
            if (vv ==false) 
                bubble.change_bubble_shape('red', 4);
            else 
                bubble.change_bubble_shape('cyan', 4);
            bubble.info = true;

                $('#id_task').val((bubble.is_within_arc(chosen_arc) === true) ? 1 : 0);
               $('#id_gamedone').val(1);

               mf(this);


//console.log((bubble.is_within_arc(chosen_arc) === true) ? 1 : 0);
             }
else fin=0;
    }} else {if (last==0) {console.log('next page'); mf(this);                     $('form#form').submit();} else {console.log('sozertsaem');}

}

}
    p.mousePressed = () => {
        console.log('mouse_ _click')
        document.dispatchEvent(myJsPsynchEvents.setup);
        document.dispatchEvent(myJsPsynchEvents.trigger);
        mf(this);
        event_happened();

    };
   // p.touchEnded = () => {
   //     event_happened();
   // }
};
//let deliver_game = () => {
//    $('#id_task').val(game);
//    // $('#form').submit();
//}
let myp5 = new p5(s, 'p5cont');
