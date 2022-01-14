from compas_rrc import (
    AbbClient,
    MoveToFrame,
    MoveToJoints,
    SetDigital,
    SetAcceleration,
    SetMaxSpeed,
    ExternalAxes,
    Motion,
    Zone,
    Stop,
    SetTool,
    SetWorkObject,
    PrintText,
    RobotJoints,
)
from compas import json_load
from compas.geometry import Vector, Frame
from compas_fab.backends import RosClient


frames = json_load(
    r"G:\My Drive\biomimetic-fabrication-clay-3dp\production\fab_data\20211129.json"
)

with RosClient() as ros:

    client = AbbClient(ros)

    client.send(SetAcceleration(100, 100))
    client.send(SetMaxSpeed(100, 250))
    client.send(SetTool("t_bf3dp_v1"))
    client.send(SetWorkObject("w_bf3dp"))

    client.send(PrintText("Press play to start"))

    client.send(Stop())
    client.send(PrintText("Moving to set start"))

    start_pos = RobotJoints([0, 20, 20, 0, 30, 0])

    client.send(MoveToJoints(start_pos, ExternalAxes(), 100, Zone.FINE))

    client.send(PrintText("Press play to run"))
    client.send(SetDigital("DO_1", 1))

    client.send(Stop())
    client.send(MoveToFrame(frames[0], 100, Zone.Z5))
    client.send(SetDigital("DO_16", 1))
    for frame in frames:
        client.send(MoveToFrame(frame, 30, Zone.Z1, motion_type=Motion.LINEAR))
    client.send(SetDigital("DO_16", 0))
    client.send(SetDigital("DO_1", 0))

    above_last_pt = frames[-1].point + Vector(0, 0, 100)
    above_last_frame = Frame(
        above_last_pt, xaxis=frames[-1].xaxis, yaxis=frames[-1].yaxis
    )
    client.send(MoveToFrame(above_last_frame, 30, Zone.Z5, motion_type=Motion.LINEAR))

    client.send(MoveToJoints(start_pos, ExternalAxes(), 100, Zone.Z10))
    client.send(PrintText("Done")from compas_rrc import (
    AbbClient,
    MoveToFrame,
    MoveToJoints,
    SetDigital,
    SetAcceleration,
    SetMaxSpeed,
    ExternalAxes,
    Motion,
    Zone,
    Stop,
    SetTool,
    SetWorkObject,
    PrintText,
    RobotJoints,
)
from compas import json_load
from compas.geometry import Vector, Frame
from compas_fab.backends import RosClient


frames = json_load(
    r"G:\My Drive\biomimetic-fabrication-clay-3dp\production\fab_data\20211129.json"
)

with RosClient() as ros:

    client = AbbClient(ros)

    client.send(SetAcceleration(100, 100))
    client.send(SetMaxSpeed(100, 250))
    client.send(SetTool("t_bf3dp_v1"))
    client.send(SetWorkObject("w_bf3dp"))

    client.send(PrintText("Press play to start"))

    client.send(Stop())
    client.send(PrintText("Moving to set start"))

    start_pos = RobotJoints([0, 20, 20, 0, 30, 0])

    client.send(MoveToJoints(start_pos, ExternalAxes(), 100, Zone.FINE))

    client.send(PrintText("Press play to run"))
    client.send(SetDigital("DO_1", 1))

    client.send(Stop())
    client.send(MoveToFrame(frames[0], 100, Zone.Z5))
    client.send(SetDigital("DO_16", 1))
    for frame in frames:
        client.send(MoveToFrame(frame, 30, Zone.Z1, motion_type=Motion.LINEAR))
    client.send(SetDigital("DO_16", 0))
    client.send(SetDigital("DO_1", 0))

    above_last_pt = frames[-1].point + Vector(0, 0, 100)
    above_last_frame = Frame(
        above_last_pt, xaxis=frames[-1].xaxis, yaxis=frames[-1].yaxis
    )
    client.send(MoveToFrame(above_last_frame, 30, Zone.Z5, motion_type=Motion.LINEAR))

    client.send(MoveToJoints(start_pos, ExternalAxes(), 100, Zone.Z10))
    client.send(PrintText("Done")
