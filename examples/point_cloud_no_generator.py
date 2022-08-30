from radariq import RadarIQ, MODE_POINT_CLOUD

"""
Example program which captures data and processes it without using a generator
"""


def point_cloud():
    try:
        riq = RadarIQ()
        riq.set_mode(MODE_POINT_CLOUD)
        riq.set_units('m', 'm/s')
        riq.set_frame_rate(5)
        riq.set_distance_filter(0, 10)
        riq.set_angle_filter(-45, 45)
        riq.start()

        while True:
            frame = riq.get_frame()
            if frame is not None:
                print(frame)

    except Exception as error:
        print(error)


#################################################################

if __name__ == '__main__':
    point_cloud()
