from pyramid.view import view_config


#def toc_view(request):
#    return Response('toc of: %s' % request.GET.get('page_url', ''))
#
#def main_view(request):
#    return Response(body='<form action="toc" method="GET">Wikipedia page: <input name="page_url" type="text"/><input type="submit" value="Submit"/></form>')
#
#if __name__ == '__main__':
#    config = Configurator()
#    config.add_route('root', '/')
#    config.add_route('toc', '/toc')
#    config.add_view(main_view, route_name='root')
#    config.add_view(toc_view, route_name='toc')
#    app = config.make_wsgi_app()
#    server = make_server('0.0.0.0', 8080, app)
#    server.serve_forever()

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'wikipedia-toc-scraper'}
