export let
    // speed = 0.2,
    correction = 0,
    centerX = 300,
    centerY = 300,
    radius = 200,
    diameter = radius * 2,
    canv_size = 600,
    arc_transparency = 200,
    length_coef = 1.5,
    arc_lengths = [1, 1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6],
    colors = ['#845EC2', '#D65DB1', '#FF6F91', '#FF9671', '#FFC75F', '#F9F871'];
    arc_lengths.forEach((i,j)=>{arc_lengths[j] = i*length_coef});


