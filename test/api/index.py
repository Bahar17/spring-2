# -*- coding: utf-8 -*-
from . import ApiHandler


class IndexRequestHandler(ApiHandler):
    def get(self):
        self.write('''
<html>
<head>
<script>
var ws=new Array()
for (var i=0;i<200;i++)
{
    ws[i] = new WebSocket('ws://0.0.0.0:8000/ws/soc');
}
ws[0].onmessage = function(event) {
    var table = document.getElementById('message');
    table.insertRow().insertCell().innerHTML = event.data;
};
</script>
</head>
<body>
<p>hi</p>
<table id='message'></table>
        ''')