# -*- coding: utf-8 -*-

from .plot_A_3D import plot_A_3D
from numpy import meshgrid, max as np_max


def plot_A_surf(
    data,
    is_deg=True,
    t_max=None,
    a_max=400,
    z_max=None,
    is_norm=False,
    unit="SI",
    colormap="RdBu_r",
):
    """Plots the isosurface of a field in 3D

    Parameters
    ----------
    data : Data
        a Data object
    is_deg : bool
        boolean indicating if the angle must be converted to degrees
    t_max : float
        maximum value of the time for the x axis
    a_max : float
        maximum value of the angle for the y axis
    z_max : float
        maximum value of the magnitude for the z axis
    is_norm : bool
        boolean indicating if the field must be normalized
    unit : str
        unit in which to plot the field
    colormap : colormap object
        colormap prescribed by user
    """

    # Set plot
    title = data.name + " as a function of time and space"
    xlabel = "Time [s]"
    if is_deg:
        ylabel = "Angle [°]"
    else:
        ylabel = "Angle [rad]"
    if unit == "SI":
        unit = data.unit
    if is_norm:
        zlabel = r"$\frac{" + data.symbol + "}{" + data.symbol + "_0}\, [" + unit + "]$"
    else:
        zlabel = r"$" + data.symbol + "\, [" + unit + "]$"

    # Extract the field
    if is_deg:
        (time, angle, Ydata) = data.get_along(
            "time", "angle{°}", unit=unit, is_norm=is_norm
        )
    else:
        (time, angle, Ydata) = data.get_along(
            "time", "angle{°}", unit=unit, is_norm=is_norm
        )

    angle_map, time_map = meshgrid(angle, time)
    
    if t_max is None:
        t_max = np_max(time)
    
    if z_max is None:
        z_max = np_max(Ydata)

    # Plot the original graph
    plot_A_3D(
        time_map,
        angle_map,
        Ydata,
        colormap=colormap,
        x_max=t_max,
        y_max=a_max,
        z_max=z_max,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        zlabel=zlabel,
        type="surf",
    )
