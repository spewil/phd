# Data Recording Protocol

## Basic Session Outline
Metadata setup (Python)
Subject Information
Filenames/folders

Calibration -- N blocks x M trials 
Is data written one file per trial…? Or appended to a file as one column per trial? What’s the best way to do this?

Data Analysis / Decoder Fitting
This doesn’t need to be automated, can be run semi-manually based on filenames
This might need some parameter tweaking 
Task Training -- J blocks x K trials 
Requires physics parameters, decoder, … 


## Cursor Physics 

H Channels of Raw EMG (Hx1) → 
Filtering (Lowpass, moving average) per channel (“u” Hx1) → 
Dot Product with decoder / projection into “dynamics space” → (“x” Dx1)

x_t = A * x_t-1 + B * u_t

B is the decoder matrix projecting from EMG electrode space (H) into “dynamics” space:
 
[x, 
y, 
v_x, 
v_y, 
f_up, 
f_down,
f_left,
f_right]

T (D=6) for physics simulation of the cursor. This feels more intuitive than a direct mapping between EMG signal to screen coordinates, which I found to be too difficult. What this allows is the EMG signal acting as a virtual force on the cursor. B (DxH) looks like

[ -- 0 -- ]
[ -- 0 -- ]
[ -- 0 -- ]
[ -- 0 -- ]
[ decoder row 1]
[ decoder row 2]
[ decoder row 3]
[ decoder row 4]

The decoder matrix is the last two rows of B, a 2xH projection matrix gleaned from the data analysis step.
