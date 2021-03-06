#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Module for calculation of Heat Index.
Heat Index or humiture or "feels like temperature" is an index thatcombines
air temperature and relative humidity in an attempt to determine the
human-perceived equivalent temperature.
Check wikipedia for more info:
    https://en.wikipedia.org/wiki/Heat_index
Formula details:
    http://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml
"""

from __future__ import division
import math



def heat_index(temperature, humidity):
    """Calculate Heat Index (feels like temperature) based on NOAA equation.
    HI is useful only when the temperature is minimally 80 F with a relative
    humidity of >= 40%.
    Default unit for resulting Temp value is Fahrenheit and it will be used
    in case of casting to int/float. Use Temp properties to convert result to
    Celsius (Temp.c) or Kelvin (Temp.k).
    :param temperature: temperature value in Fahrenheit or Temp instance.
    :type temperature: int, float, Temp
    :param humidity: relative humidity in % (1-100)
    :type humidity: int, float
    :returns: Heat Index value
    :rtype: Temp
    """

    c1 = -42.379
    c2 = 2.04901523
    c3 = 10.14333127
    c4 = -0.22475541
    c5 = -6.83783e-3
    c6 = -5.481717e-2
    c7 = 1.22874e-3
    c8 = 8.5282e-4
    c9 = -1.99e-6

    T = (temperature * 9 / 5. ) + 32

    RH = humidity
  #  print('temp, humidity:', T,',',RH)
    # try simplified formula first (used for HI < 80)
    HI = 0.5 * (T + 61. + (T - 68.) * 1.2 + RH * 0.094)
 #   print('Heat Index 1:', HI)

    if T >= 80:
        # use Rothfusz regression
        HI = math.fsum([
            c1,
            c2 * T,
            c3 * RH,
            c4 * T * RH,
            c5 * T*T,
            c6 * RH*RH,
            c7 * T*T* RH,
            c8 * T * RH*RH,
            c9 * T*T * RH*RH,
        ])
        
    HIc=(HI-32)*5/9
#    print('Heat Index 2:', HI)
    return HIc

