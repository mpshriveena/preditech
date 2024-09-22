<template>
    <div class="body">
      <div class="inbody">
          <h2 class="logo"><strong>About PrediTech<i class='bx bx-rupee'></i></strong></h2>
          <div class="content">
            <h4>Welcome to PrediTech!! This is our house price prediction tool designed to help you estimate property values 
    with ease. PrediTech uses advanced data analytics to predict the house prices based on key features such as 
    overall quality, living area, garage cars, garage size, and basement area.
    PrediTech offers accurate insights to assist you in making informed decisions for your real-estate business.
</h4>
<h4>
To use this tool, click on "Predict" Now button on the home page. You can also navigate to Prediction page through "Predict" route in Nav Bar.
Enter the values such as Overall Quality (from 0 to 10), Ground Living Area, Garage Cars, Garage Area and Total Basement (in Square Feet). 
After entering the values, click on "Predict" button to predict the Sales Price of the house.
</h4>
          <div class="footer">
                  <p>&copy; 2024 PrediTech. All rights reserved.</p>
              </div>
      </div>
  </div>
      </div>
  </template>

<style scoped>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', 'sans-serif';
}
.body{
    margin:0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Poppins', 'sans-serif';
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      background: rgb(227, 194, 247)
}
.inbody{
    background: rgba(255, 255, 255, 1);
    padding: 5%;
    border-radius: 10px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
    width: 90%;
    min-height: 80vh;

    
  }
  .logo{
    color:rgb(121, 7, 197);
      text-align: center;
    }
    .content{
        margin-top:3%
    }
h4{
    text-align:justify ;
}
.footer{
text-align:center;
margin-top:5%;
}
</style>
  