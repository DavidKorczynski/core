import os
import sys

blue = "#052569"
orange = "#f5821f"
green = "#79A442"
grey = "#92B3B7"
off_white = "#E5E5E5"
off_orange = "#F9AB2D"

color_names = {
    blue: "blue",
    orange: "orange",
    green: "green",
    grey: "grey",
    off_white: "off_white",
    off_orange: "off_orange",
}

orange_blue = {"head": orange, "body": blue}
blue_blue = {"head": blue, "body": blue}
orange_green = {"head": orange, "body": green}
green_blue = {"head": green, "body": blue}
grey_blue = {"head": grey, "body": blue}
dark_mode = {"head": off_orange, "body": off_white}

normal = {"arms": "down", "legs": "straight"}
out = {"arms": "out", "legs": "out"}
angled = {"arms": "angled", "legs": "straight"}
up = {"arms": "up", "legs": "straight"}
up_out = {"arms": "up", "legs": "out"}

colors = [orange_blue, blue_blue, orange_green, green_blue, grey_blue, dark_mode]
sizes = [8, 16, 32, 64, 128]
poses = [normal, out, angled, up, up_out]

opts = ["", "--no-margins"]

for size in sizes:
    diameter = size * 2
    width = diameter * 14
    height = diameter * 14
    dimensions = f"{width}x{height}"

    radius_opt = f"--radius {size}"
    os.makedirs(f"./{dimensions}", exist_ok=True)
    for color in colors:
        head = color["head"]
        body = color["body"]
        color_opts = f"--head '{head}' --body '{body}'"
        head = color_names[head]
        body = color_names[body]
        for pose in poses:
            arms = pose["arms"]
            legs = pose["legs"]
            pose_opts = f"--arms {arms} --legs {legs}"
            for opt in opts:
                command = f"python3 agentsvg.py {color_opts} {pose_opts} {radius_opt} {opt}"
                if opt:
                    opt = opt.replace("--", "").replace("-", "_")
                base_name = f"agent_{head}_{body}_{arms}_{legs}_{dimensions}" + (f"_{opt}" if opt else "")
                generate = f"{command} > ./{dimensions}/{base_name}.svg"
                convert = f"convert -background none ./{dimensions}/{base_name}.svg ./{dimensions}/{base_name}.png"
                command = f"{generate} && {convert}"
                print(command)
                ret = os.system(command)
                if ret != 0:
                    sys.exit("Error: The command above failed! (Non-zero exit code)")
