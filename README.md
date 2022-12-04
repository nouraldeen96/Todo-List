<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css">
    <link rel="stylesheet" href="{{url_for('static', filename='css/stylesheet.css')}}">
    <title>{{title}}</title>
    {% if custom_css %}
    <link rel="stylesheet" href="{{url_for('static', filename='css/' + custom_css + '.css')}}">
    {% endif %}
</head>
<body>
    <header>
        <div class="logo">
            <h1 class="logo1">TODO</h1>
            <img class="img-logo" src="{{url_for('static',filename='images/inventory-190.png')}}"/>
        </div>
        <nav class="nav">
            <a class="all" href="all tasks">ALL</a>
            <a href="todo">ToDo</a>
            <a href="progress">Progress</a>
            <a href="done">Done</a>
            <a href="important">Important</a>
        </nav>

    </header>
    <section>
      {%block body%}
      <section>
      {{title1}}
      </section>
      {%endblock%}
   
        
    </section>

    
</body>
</html>
