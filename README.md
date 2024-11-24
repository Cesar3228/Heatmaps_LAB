# Heatmaps_LAB
Data comes from research conducted at the Faculty of Sciences of the National Autonomous University of Mexico (UNAM) in Mexico City [future link to the paper]. This study aimed to evaluate the resilience to stress that the offspring of exercised and enriched female mice would have. Resilience to stress was measured by anxiety and depressive-like behaviors. Anxiety-like behavior was evaluated using a maze called the Elevated Plus Maze. The Elevated plus Maze is a behavioral test used in pre-clinical research for measuring anxiety-like behavior. Mice are placed by the experimenter at the center of an elevated four arms maze. Two arms of the maze are enclosed within walls, and the remaining two arms are open. Entries and duration in each arm,  and path travelled throughout the maze are recorded by a video-tracking system for 5 min. An increase on exploration and time spent in open arms reflects an anti-anxiety behavior. A commercial video tracking system called ANY-maze was used. this video tracking system and others alike records the coordinates of the tracking subject several times thoughout the test. This trackplot was exported into a .csv for each mouse of each experimental group and then analyzed to generate a heatmap and/or density map  for each experimental group. Six heatmaps were generated for the 6 experimental groups. Each heatmap indicates  the density of mice activity from each experimental group.

------------

## Repository Layout


### 1.- Graphs Folder

- This folder contains the 6 density position graphs that were obtain with data and functions.


### 2.- Jupyter Notebooks Folder

- This folder contains the Jupyter Notebooks that were used for each density position graphs. They use the functions in the HeatmapTools.py document that is in the "Python Functions (Code)" folder

  
### 3.- Python functions (Code) folder

- This folder contains the HeatmapTools.py with the functions that were created from the original script and were used to obtain the graphs.

------------

## Functions Explanation

This is a brief explanation on how the function work.

  - From line 1-15: Contains the if statement and libraries used.
  - From line 18-31: The "cargar_prepara_archivos" function loads all csv files from a speccified directory, concatenates them into a single dataframe, removes the NA values and resets the index for the new dataframe.
  - From line 36-50: The "normalizar_coordenadas" function normalizes X and Y coordinates in the input dataframe(df) to match the scale of the reference dataframe (ref_df).
  - From line 53-57: The "combinar_dfs" function combines two dataframes.
  - From line 62-119: The "plot_heatmap_overlay" function creates a heatmap overlaing the spatial distribution of points on a maze image. The important points of this function are the "Kernel Density Estimation(KDE)" which computes a KDE using gaussian_kde and dynamically adjusts the bandwith using bw_method, the "Density Scaling" which calculates KDE values at the X and Y points and sets optimal parameters(vmin_opt, vmax_opt) that go from blue to red.



The main code was written by Cesar3228, the Data was obtain by Jimena A. for her masters degree, the functions were compiled by Santiago R. and all the work was verify by Jimena A. and Monserrat S.
