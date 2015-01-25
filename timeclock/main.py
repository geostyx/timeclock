from timeclock import client


def main():
    # Create and start a new instance of the app
    my_app = client.App()
    my_app.start()


if __name__ == '__main__':
    main()