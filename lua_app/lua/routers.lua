local routers = {
    {
        'views', -- app name
        {
            { '/panel/games', 'panel.games' },
            { '/panel', 'panel.index' },
        } -- app routers
    },
}

return routers