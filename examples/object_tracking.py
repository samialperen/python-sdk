from radariq import RadarIQ, MODE_OBJECT_TRACKING

"""
Example program which receives object tracking frames
"""


def object_tracking():
    try:
        riq = RadarIQ()
        riq.set_mode(MODE_OBJECT_TRACKING)
        riq.set_units('m', 'm/s')
        riq.set_frame_rate(5)
        riq.set_distance_filter(0, 10)
        riq.set_angle_filter(-45, 45)
        riq.start()

        for frame in riq.get_data():
            if frame is not None:
                print(frame)

    except Exception as error:
        print(error)


#################################################################

if __name__ == '__main__':
    object_tracking()
