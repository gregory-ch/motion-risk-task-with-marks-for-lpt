

function animation(args, elem) { // некоторые аргументы определим на будущее
//   document.body.style.background = 'green';



        var bls=0;
	var $ = {
              		speed   :     250 // скорость/задержка ( в js это мс, например 10 мс = 100 кадров в секунду)
	}
	var f = 0;
	var colour = 0;
	var change=0;
	elem.style.background = 'blue';
	var s = 250; //Вычислим угол
	setInterval(function() { // функция движения 
		f += s; // приращение аргумента
console.log(f);
//		elem.style.left =  100  + 'px'; // меняем координаты элемента, подобно тому как мы это делали в школе в декартовой системе координат. Правда, в данном случае используется полярная система координат, изменяя угол
//		elem.style.top =   100  + 'px';
		colour = Math.floor(3*Math. random());//Math.sin(f);
		if ((f>2000)&&(f<12000)){
			if (colour == 2)   {  
				if (change ==0) {change=1;bls=bls+1;
					document.getElementById("id_bls").setAttribute('value',bls);
					elem.style.background = 'green';
					console.log(bls);
					}		
    				//$('#id_bls').val(5);
			}
			if (colour == 1)    elem.style.background = 'blue';
			if (colour == 0)    elem.style.background = 'cyan';
	                if(colour <2) change=0;
		}
//		if (f>15000)  {var form=document.getElementById("form");
//form.submit();
	}, $.speed)
}
              

window.onload =function(){
	animation({}, document.getElementById("oo"));
        };
