class AuthorizationMiddleware(object):

    def resolve(self, next, root, info, **args):
        args['user'] = info.context.data.pop('user')
        return next(root, info, **args)