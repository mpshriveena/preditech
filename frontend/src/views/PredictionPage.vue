<template>
    <div class='body'>
            <div class="signup-box">
          <form @submit.prevent="predict">
            <h1><strong>Predict Price</strong></h1>
            <h5>Provide the below details to predict the price of your house</h5>
          <br>  <h6>Overall Quality (Rate from 0 to 10)</h6>
            <div class = "inputbox">
              
              <input type="number" id="overall_quality" placeholder="9" v-model="overall_quality" required>
            </div>
            <div v-if="errors.error1" class="error-message">{{ errors.error1 }}</div>

            <h6>Ground Living Area</h6>

            <div class = "inputbox">             
              <input type="number" id="gr_liv_area" placeholder="500" v-model="gr_liv_area" required>
            </div>
            <div v-if="errors.error2" class="error-message">{{ errors.error2 }}</div>

            <h6>Garage Cars</h6>
            <div class = "inputbox">
              <input type="number" id="garage_cars" placeholder="2" v-model="garage_cars" required>
            </div>
            <div v-if="errors.error3" class="error-message">{{ errors.error3 }}</div>

            <h6>Garage Area</h6>
            <div class = "inputbox">
              <input type="number" id="garage_area" placeholder="500" v-model="garage_area" required>
            </div>
            <div v-if="errors.error4" class="error-message">{{ errors.error4 }}</div>

            <h6>Total Basement (in Square feet)</h6>

            <div class = "inputbox">
              <input type="number" id="total_bsmt_sf" placeholder="500" v-model="total_bsmt_sf" required>
            </div>
            <div v-if="errors.error5" class="error-message">{{ errors.error5 }}</div>

              <button class="button" @click='Predict'> Predict </button>
           <br><br>   <div v-if="predicted_price" class="predicted-price">
        <h5>Predicted Price: {{ predicted_price }}</h5>
            </div>
            </form>
            
          </div>
        </div>
  </template>

<script>
import axios from 'axios';
export default {
    data(){
        return{
          overall_quality:0,
          gr_liv_area:0,
          garage_cars:0,
          garage_area:0,
          total_bsmt_sf:0,
          predicted_price:0,
          errors:{},
        }
    },
    methods:{
      async Predict() {
  try {
    const response = await axios.post('http://127.0.0.1:5000/predict', {
      overall_quality: this.overall_quality,
      gr_liv_area: this.gr_liv_area,
      garage_cars: this.garage_cars,
      garage_area: this.garage_area,
      total_bsmt_sf: this.total_bsmt_sf
    });
    this.predicted_price = response.data.predicted_price;
    
    this.errors = {}; // Clear errors if prediction is successful
      } 
      catch (error) {
        if (error.response && error.response.status === 404) {
          this.errors = error.response.data; // Capture all errors
        }
  }
}
    }
}
</script>

<style scoped>
    .body {
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
    .signup-box{
      background: rgba(255, 255, 255, 1);
    border-radius: 10px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
    min-width: 40%;
    min-height: 80vh; 
      display:flex;
      justify-content:center;
      align-items:center;
      color:rgb(0, 0, 0);
      padding:3%;
    }
    .signup-box h1{
      font-size:32px;
      text-align:center;
      text-shadow: 3px 3px 8px rgb(133, 133, 132); 
    
    }
    .signup-box .inputbox{
      position:relative;
      width:100%;
      height: 40px;
      border-bottom:2px solid rgb(0, 0, 0);
      
    }
    
    .inputbox input{
      width:100%;
      height: 100%;
      background:transparent;
      border:none;
      outline: none;
      color: rgb(0, 0, 0);
    }
    .inputbox ::placeholder{
      color:rgb(184, 184, 184);
    }
    
    
    .button{
      margin-top:20px;
      width:100%;
      height:45px;
      background:rgb(121, 7, 197);
      border:none;
      outline:none;
      color:white;
      border-radius: 4px;
      cursor:pointer;
      font-weight:500;
      text-shadow: 3px 3px 8px rgb(0, 0, 0);
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    }
    .button:hover{
      background: rgb(80, 2, 133);
      box-shadow: 0 0 7px 7px rgb(80, 2, 133, 0.5);
    }
    .signup-box {
      font-size: 14.5px;
      font-weight: 500;
      margin-top: 25px;
      color: rgb(0, 0, 0);
    }
    
    h1{
      color:rgb(121, 7, 197);
    }
    .error-message {
  color: red;
  font-size: 14px;
}
h6 {
  margin: 0; /* Remove default margin */
  margin-top:10px;
}
    @media screen and (max-width: 768px) {


.signup-box{
  min-height:50vh;
  width:90%;
}


    }
    
</style>
