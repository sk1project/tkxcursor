#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Copyright (C) 2009 by Igor E. Novikov
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA


import os, Tkinter, tkXcursor

frames=[]	
cursors=[]

def loadCursors(widget, path):
	cursors=[]
	files = os.listdir(path)
	for file in files:
		if os.path.isfile(path+file):
			cursors.append(tkXcursor.load_cursor(widget, path+file))
	return cursors
		
def setCursors(*args):
	i=0
	if tkXcursor.is_xcursor_supported(root):
		for frame in frames:
			tkXcursor.set_cursor(frame, cursors[i])
			i+=1


root=Tkinter.Tk()
text=Tkinter.Label(root,text='To view custom cursors just move\n mouse pointer over the frames:', font='Arial 10')
text.pack(side="top")

cursors=loadCursors(root, './cursors/')

for cursor in cursors:
	frame=Tkinter.Frame(root, width=200,height=50, bg="white")
	frame.pack(side="top", padx=5, pady=5)
	frames.append(frame)

#Please note we works directly with X11 server so ARGB cursor should be 
#applied only after widget exposing on screen. If you will try setting cursor 
#before widget exposing i.e. before real widget creation on X server side 
#you will get BadWindow exception and your application will be terminated
frames[-1].bind('<Visibility>',setCursors)

root.mainloop()