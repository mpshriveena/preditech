<template>
    <div class="home">
      <div class="inhome">
     
        <div class="hello">
          <div class="content">
            <h2 class="logo"><strong><i class='bx bx-rupee'></i> PrediTech</strong></h2>
          </div>
            <div class="text-sci">
              <h1> Welcome ! !<br><strong> To our House Price Predictor</strong></h1>
              <p>The world of real estate can be complex and unpredictable. 
   That's where Preditech comes in, simplifying the process with accurate house price predictions. 
   We leverage advanced data analytics to provide reliable insights into property values anytime, anywhere! 
   Please visit the "About" page 
   to learn how to use this tool. Happy Predicting with Preditech!!</p>
            </div>
            <div class="buttondiv">
            <button class="button" @click='PredictPage'> Predict Now</button>
          </div> </div>
        </div>
    </div>
    </template>

<script>
import axios from 'axios';

export default {
  
  methods:{
    PredictPage(){
    this.$router.push({ path: `/predictprice` });
  },
  }
}
</script>
<style scoped>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', 'sans-serif';
}
    .home{
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
.inhome{
    background: rgba(255, 255, 255, 1);
    
    border-radius: 10px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
    width: 90%;
    min-height: 70vh;

    
  }
    
    .hello .content{
      font-size:30px;
    
    }
    .home .hello{
      width:100%;
      height: 100%;
      background:transparent;
      padding: 12%;
      color:rgb(0, 0, 0);
    }
    
    
    
    .hello .content h2 {
      font-size: 30px;
      text-shadow: 3px 3px 8px rgba(0, 0, 0, 0.616);
    }
    
    .text-sci h1 {
      font-size: 40px;
      text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.452); 
    }
    
    .text-sci p {
      font-size: 22px;
      margin: 20px 0;
      color: rgb(66, 66, 66);
      text-shadow: 5px 5px 15px rgba(0, 0, 0, 0.5);
      padding: 10px;
      border-radius: 5px; 
    }
    .buttondiv{
      display:flex;
      justify-content: center;
    }
    .button{
      width:25%;
      height:50px;
      background:rgb(121, 7, 197);
      border:none;
      outline:none;
      color:white;
      border-radius: 4px;
      cursor:pointer;
      font-size: 22px;
      font-weight:500;
      text-shadow: 3px 3px 8px rgb(0, 0, 0);
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    }
    .button:hover{
      background: rgb(80, 2, 133);
      box-shadow: 0 0 7px 7px rgb(80, 2, 133, 0.5);
    }
    
    .logo{
      color:rgb(121, 7, 197);
    }
    @media screen and (max-width: 768px) {
.inhome{
  padding:5%
}
      .home .hello {
        padding: 0; 
    }
.button{
      width:75%;
      height:50px;

    }
  }
    
    </style>


