# mimaze

driver
	init logs
	read configs command line and/or from file
	start the maze class

maze module
	class setMaze
		Init the terrain

	class initMaze
		build rooms here from vector maps and/or random rooms/tunnels

	class buildMaze
		Build a bunch of rooms
		Connect the rooms with tunnels
		Determine start/end points
		
		
	class rooms
		walls[]
		doors[]

	class walls
		blocks[]
		direction - N, S, E, W to begin, then more complicated NE, SE, etc. for 45 deg walls

	class block
		x
		y
		z
		blockType
		blockData

	class doors
		directon
		size

	class tunnel
		radius
		direction
		start
		end
