
def html():
    from cloudant.client import Cloudant
    from cloudant.error import CloudantException
    from cloudant.result import Result, ResultByKey
    import time as t
    client = Cloudant("5e42a7d0-ea17-4a3a-bbbf-2cd472931bd0-bluemix", "efe6af61c9872c02b29eb078f9ac872e5fcf41afaa1333bdef1f8ff88d9de508", url="https://5e42a7d0-ea17-4a3a-bbbf-2cd472931bd0-bluemix:efe6af61c9872c02b29eb078f9ac872e5fcf41afaa1333bdef1f8ff88d9de508@5e42a7d0-ea17-4a3a-bbbf-2cd472931bd0-bluemix.cloudantnosqldb.appdomain.cloud")
    client.connect()
    my_database = client.create_database("url")
    #dtt=[]
    result_collection = Result(my_database.all_docs, include_docs=True)
    liss=['URL','Property','Domain','Registrar','Organisation','Alexa Rank','Address','City','State','Zipcode','Country','E-mails','time']
    
    
    html_p="""<!DOCTYPE html><html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.11.2/css/all.css">
    <!-- Google Fonts Roboto -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap">
    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="static/css/bootstrap.min.css">
    <!-- Material Design Bootstrap -->
    <link rel="stylesheet" href="static/css/mdb.min.css'">
    <!-- Your custom styles (optional) -->
    <link rel="stylesheet" href="static/css/style.css">
    <!-- MDBootstrap Datatables  -->
    <link href="static/css/addons/datatables2.min.css" rel="stylesheet">
    <title>Malicious URL Detector</title>
    <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <!-- Bootstrap CSS -->
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
  <!-- Bootstrap core CSS -->
  <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
  <!-- Material Design Bootstrap -->
  <link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.10.1/css/mdb.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/limonte-sweetalert2/8.11.8/sweetalert2.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/limonte-sweetalert2/8.11.8/sweetalert2.all.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/promise-polyfill"></script>

  <link rel="icon" href="{%static '46-512.png' %}" type="image/png">
  <title>{% block title %}Malicious URL Detector{% endblock %}</title>

    </head>
        
    <body>
    <!--Navbar-->



  <nav class="navbar navbar-expand-lg navbar-dark primary-color fixed-top scrolling-navbar" >

    <!-- Navbar brand -->

    <!-- Collapse button -->
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#basicExampleNav"
      aria-controls="basicExampleNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <!-- Collapsible content -->
    <div class="collapse navbar-collapse" id="basicExampleNav">

      <!-- Links -->
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <a class="nav-link" href="/">Home
            <span class="sr-only">(current)</span>
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'geturlhistory' %}">URL History Database</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'fetchanalysis' %}">Live Data Analysis</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'testresults' %}">Test Results</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'getuserfeedbackform' %}">User FeedBack</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'discuss' %}">Discuss Channel</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'getdataset' %}">Download Dataset(URL History)</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'cloudantcsv' %}">CloudantDataset</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'about' %}">About Application</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% static 'chrome-ext.zip' %}" download>Download Chrome Extension</a>
        </li>
      </ul>
      <!-- Links -->
    </div>
    <!-- Collapsible content -->

  </nav>
  <!--/.Navbar-->
</br></br>
</br>
</br>
</br>
    <h2 class='mb-3' style="text-align:center;color:blue">Dataset (Blacklisting purpose)</h2>
    <table id="dtBasicExample" class="table" width="100%" >
    
    <thead>
        <tr>
        <th>Index Number</th>
        <th>URL</th>
        <th>Status</th>
        <th>Domain</th>
        <th>Registrar</th>
        <th>Organisation</th>
        <th>Alexa Rank</th>
        <th>Address</th>
        <th>City</th>
        <th>State</th>
        <th>Zip Code</th>
        <th>Country</th>
        <th>Email</th>
        <th>Time</th>
        </tr>
    </thead>
    <tbody>"""
    
    # for result in result_collection:
    #     url=str(result['doc']['URL'])
    #     status=str(result['doc']['Property'])
    #     name=str(result['doc']['Name'])
    #     org=str(result['doc']['Organisation'])
    #     add=str(result['doc']['Address'])
    #     city=str(result['doc']['City'])
    #     state=str(result['doc']['State'])
    #     ziip=str(result['doc']['Zipcode'])
    #     country=str(result['doc']['Country'])
    #     email=str(result['doc']['E-mails'])
    #     dom=str(result['doc']['Domain'])
    #     rank=str(result['doc']['Alexa Rank'])
    #     reg=str(result['doc']['Registrar'])
    #     time=str(result['doc']['time'])
    #     a=[url,status,name,org,add,city,state,ziip,country,email,dom,rank,reg,time]
    #     dtt.append(a)
    #     t.sleep(0.0001)
    ii=0
    import csv
    with open("static/cloudant_count2.csv", "r") as f:
        for row in f:
            cot=int(row)
    cott=cot-2000
    res=result_collection[cott:]
    for result in res:
        ii=ii+1
        html_p=html_p+"<tr>"
        html_p=html_p+"<td>"+str(ii)+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['URL'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['Property'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['Domain'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['Registrar'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['Organisation'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['Alexa Rank'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['Address'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['City'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['State'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['Zipcode'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['Country'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['E-mails'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['time'])+"</td>"
        html_p=html_p+"</tr>"
        t.sleep(0.0000001)

    html_p=html_p+"""</tbody></table></br></br>
    <!-- End your project here-->
    <div class="container-fluid">
      <!-- Footer -->
      <footer class="page-footer font-small blue fixed-bottom">
        <!-- Copyright -->
        <div class="footer-copyright text-center py-3"
          style="background: black;color: white;font-weight:bold;font-size:0.5rem;">
          <span>© 2020 Copyright: <a href="https://abhisheksportfolio.herokuapp.com/">Abhishek Saxena&nbsp;&nbsp;
            <a class="ins-ic" href="https://github.com/abhisheksaxena1998"><i class="fab fa-github  fa-3x"></i></a></span>
            
        </div>
        <!-- Copyright -->
      </footer>
      <!-- Footer -->
    </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <!-- JQuery -->
    <!-- JQuery -->
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <!-- Bootstrap tooltips -->
    <script type="text/javascript"
      src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.4/umd/popper.min.js"></script>
    <!-- Bootstrap core JavaScript -->
    <script type="text/javascript"
      src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <!-- MDB core JavaScript -->
    <script type="text/javascript"
      src="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.10.1/js/mdb.min.js"></script>
      
</body>

</html>

    <!-- jQuery -->
    <script type="text/javascript" src="static/js/jquery.min.js"></script>
    <!-- Bootstrap tooltips -->
    <script type="text/javascript" src="static/js/popper.min.js"></script>
    <!-- Bootstrap core JavaScript -->
    <script type="text/javascript" src="static/js/bootstrap.min.js"></script>
    <!-- MDB core JavaScript -->
    <script type="text/javascript" src="static/js/mdb.min.js"></script>
    <!-- MDBootstrap Datatables  -->
    <script type="text/javascript" src="static/js/addons/datatables2.min.js"></script>
    <script>
    $(document).ready(function () {
    $('#dtBasicExample').DataTable();
    $('.dataTables_length').addClass('bs-select');
    });
    </script>

    </body>
    </html>"""
    return html_p