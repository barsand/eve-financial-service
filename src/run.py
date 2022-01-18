import eve
import settings

app = eve.Eve(settings={
    'DOMAIN': settings.DOMAIN
})

if __name__ == '__main__':
    app.run()
