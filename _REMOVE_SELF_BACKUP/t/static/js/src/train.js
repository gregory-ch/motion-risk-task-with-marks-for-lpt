//TODO: move bubbles and arcs into sep class and export using require, module.export
import p5 from "./p5";
import {Bubble} from './bubble';
import {Arc, ChoosableArc} from './arc';
import *  as c from './constants';
import jspsych from "./jspsych";

let bubble,
    game,
    arcs = [];
let keyCode;


let countwin=9;
let timerestout=timerestin;
var tmp = document.getElementById('tmp');
var   results = document.getElementById('result');

console.log(timerestin);
var currentTime=0;
var currentTime2=0;
console.log('v16');


window.onload=function () {currentTime= new Date(); }

function mf(){ currentTime2= new Date();
timerestout=timerestin-Math.floor(currentTime2-currentTime);
$('#timerest').val(timerestout);
console.log(timerestout);

}


                setTimeout(function () {mf(this);
console.log('timerestin>>');console.log(timerestin);
sendMessage('I');
console.log('mark 25');

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
    //    if (choose_difficulty === false) {
            chosen_arc = arcs[chosen_arc_id];
            chosen_arc.chosen = true;
            chosen_arc.do_if_clicked();
    //    }
        
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
        if (typeof chosen_arc_id =='undefined') {chosen_arc_id=0; }
  
//        let in_canvas = (p.mouseX > 0 && p.mouseX < c.canv_size && p.mouseY > 0 && p.mouseY < c.canv_size);
//        if (in_canvas) {
            if (choose_difficulty === true) {
                arcs.forEach((i, j) => {
                    if (i.id==chosen_arc_id) {
                        arcs.forEach((l, m) => {
                            l.chosen = false
                        });
                        i.chosen = true;
                        i.do_if_clicked();

                    }
                });
            } else {

                arcs.forEach(l => l.set_transparency(80));
                let old_speed = speed;
                speed = 0;

                let vv=bubble.is_within_arc(chosen_arc);
                if (vv ==false) 
                {bubble.change_bubble_shape('red', 4);               results.innerHTML ='Вы проиграли';sendMessage('K'); console.log('mark 27');}
                else 
                {bubble.change_bubble_shape('cyan', 4);  countwin=chosen_arc_id;             results.innerHTML ='Вы выиграли '+countwin+' баллов'; sendMessage('L');console.log('mark 28');}
                bubble.info = true;
                $('#id_task').val((bubble.is_within_arc(chosen_arc) === true) ? 1 : 0);
                $('#id_gamedone').val(1);
                mf(this);

            }
//        }
    }
    p.mousePressed = () => {
//        event_happened();
    };
    p.keyPressed = function() {
     if(p.keyCode == 39 && chosen_arc_id>0 && choose_difficulty === true) {
     chosen_arc_id=chosen_arc_id-1;
     mf(this);
     sendMessage('M');
     console.log('mark 29');
     event_happened();
    }
    
    if(p.keyCode == 37 && chosen_arc_id<9 && choose_difficulty === true) {
     chosen_arc_id=chosen_arc_id+1;
     mf(this);
     sendMessage('N');
     console.log('mark 30');
     event_happened();
    }
    if(p.keyCode == 40 && choose_difficulty === true) {
     mf(this);
     sendMessage('O');
     console.log('mark 31');
     $('form#form').submit();

    }
    if(p.keyCode == 40 && choose_difficulty === false) {
     sendMessage('P');
     console.log('mark 32');
     event_happened();
                setTimeout(function () {  mf(this);
                    $('form#form').submit();
                }, 3000);
    }
//    return false; // prevent default
    };

//    p.touchEnded = () => {
//        event_happened();
//    }
};
//let deliver_game = () => {
//    $('#id_task').val(game);
    // $('#form').submit();
//}
let myp5 = new p5(s, 'p5cont');
