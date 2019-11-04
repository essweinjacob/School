<!DOCTYPE html>
<html lang="en">
<head>
    <title>Registration</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="../CSS/styles.css">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	<script src="../JavaScript/script.js"></script>
</head>
<style>
    body {background-color: lightgrey;}

    ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
        width: 100%;
        background-color:sandybrown;
    }

    li a {
        display: block;
        color: #000;
        padding: 8px 16px;
        text-decoration: none;
    }

    /* Change the link color on hover */
    li a:hover {
        background-color: #555;
        color: white;
    }

</style>
<body>

<div class="container-fluid text-center">
    <div class="row content">
        <div class="col-xs-12 col-sm-3 col-md-3 col-lg-3 sidenav">
            <div>
                <h1>Navigation</h1>
                <ul>
                    <li><a href="#home" onclick="location.href='./index.html';">Home</a></li>
                    <li><a href="#registration" onclick="location.href='./registration.html';">Registration</a></li>
                    <li><a href="#animations"onclick="location.href='./animations.html';">Animations</a></li>
                </ul>
            </div>
        </div>
        <form action="/to_the_server" method="POST">
            <div class="col-xs-12 col-sm-9 col-md-9 col-lg-9 text-left">
                <div class="row">
                    <div class="col-xs-12 col-sm-12 col-md-6">

                        <div class="form-group">
                            <label for="fname">First Name:</label>
                            <input id="fname" name="fname" class="form-control"
                                   type="text" onblur="fnv()" placeholder="Enter First Name Here" required/>
                            <p id="fnback"></p>
                        </div>
                        <div class="form-group">
                            <label for="lname">Last Name:</label>
                            <input id="lname" name="lname" class="form-control"
                                   type="text" onblur="lnv()" placeholder="Enter Last Name Here" required/>
                            <p id="lnback"></p>
                        </div>
                        <div class="form-group">
                            <label for="a1">Address Line 1:</label>
                            <input id="a1" name="a1" class="form-control"
                                   type="text" onblur="a1v()" placeholder="Enter Address here" required/>
                            <p id="a1back"></p>
                        </div>
                        <div class="form-group">
                            <label for="a2">Address Line 2:</label>
                            <input id="a2" name="a2" class="form-control"
                                   type="text" onblur="a2v()" placeholder="Enter Address here"/>
                            <p id="a2back"></p>
                        </div>
                        <div class="form-group">
                            <label for="city">City:</label>
                            <input id="city" name="city" class="form-control"
                                   type="text" onblur="cityv()" placeholder="Enter city here" required/>
                            <p id="cityback"></p>
                        </div>

                        <div class="form-group">
                            <label for="state">State:</label>
                            <select id="state" name="state" class="form-control" required>
                                <option value="" selected="selected" hidden="hidden" disabled="disabled">
                                    --Please Select--
                                </option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="zip">Zip:</label>
                            <input id="zip" name="zip" class="form-control"
                                   type="text" onblur="zipFormat()" placeholder="xxxxx-xxxx" required/>
                            <p id="zback"></p>

                        </div>
                    </div>
                    <div class="col-xs-12 col-sm-12 col-md-6">

                        <div class="form-group">
                            <label for="gender">Gender:</label>
                            </br>
                                <input name="gender" type="radio" onclick="gend(this.value)" value="Male" required> Male<br>
                                <input name="gender" type="radio" onclick="gend(this.value)" value="Female"> Female<br>
                                <input name="gender" type="radio" onclick="gend(this.value)" value="Other"> Other<br>
                        </div>
                        <div class="form-group">
                            <label for="mstatus">Marital Status:</label>
                            </br>
                                <input name="mstatus" onclick="mstat(this.value)" type="radio" value="Single" required>Single<br>
                                <input name="mstatus" onclick="mstat(this.value)" type="radio" value="Married">Married<br>
                                <input name="mstatus" onclick="mstat(this.value)" type="radio" value="Divorced">Divorced<br>
                        </div>
                        <div class="form-group">
                            Date of Birth:
                            <input type="date" id="myDate" onblur="birthv()" name="date" required>
                        </div>
                        <div class="form-group">
                            <label for="username" >Username: </label>
                            <input id="username" name="username" class="form-control"
                                   type="text" onblur="unv()" placeholder="Enter Username here" required/>
                            <p id="unback"></p>

                        </div>
                        <div class="form-group">
                            <label for="password">Password:</label>
                            <input id="password" name="password" class="form-control"
                                   type="password" onblur="pwv()" placeholder="Enter Password here" required/>
                            <p id="pback"></p>
                        </div>
                        <div class="form-group">
                        <label for="password">Repeat Password:</label>
                            <input id="rpassword" name="password" class="form-control"
                               type="password" onblur="rpwv()" placeholder="Repeat Password here" required/>
                        <p id="rpback"></p>
                         </div>
                        <div class="form-group">
                            <label for="email">Email:</label>
                            <input id="email" name="email" class="form-control"
                                   type="email" onblur="emv()"placeholder="email@domain.com" required/>
                            <p id="eback"></p>
                        </div>
                        <div class="form-group">
                            <label for="tel">Phone:</label>
                            <input id="tel" name="tel" class="form-control"
                                   type="tel" onblur="phoneFormat()" placeholder="xxx-xxx-xxxx" required/>
                        </div>
                        <p id="pnback"></p>
                        <input type="submit" class="btn btn-success" value="Submit" onclick="validate()">
                        <p id="failed"></p>
                        <input type="reset" class="btn btn-info" value="Reset">
                    </div>
                </div>
            </div>
        </form>
    </div>
</div>

<footer class="container-fluid text-center">

</footer>

</body>
</html>