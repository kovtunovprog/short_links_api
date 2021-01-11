from loader import app


def main():
    from apps import routes
    import sys
    try:
        if sys.argv[1] == 'db_startup':
            from utils.db_api import db_startup
            db_startup()
            return
    except IndexError:
        pass
    app.run(debug=True)


if __name__ == '__main__':
    main()
