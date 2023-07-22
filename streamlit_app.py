
import streamlit  as st
import joblib
import pandas as pd

Model = joblib.load("Model.pkl")
Inputs = joblib.load("Inputs.pkl")

def prediction(Airline , Source , Destination ,
               Month_of_Journey_Num , Day_of_Journey_Num ,
               Distance , Stops_Counts , Dep_Hour , Categorized_Duration,
               Meal, Arrival_Hour, Arrival_Day_Period,
       Dep_Day_Period):
    test_df = pd.DataFrame(columns=Inputs)
    test_df.at[0,"Airline"] = Airline
    test_df.at[0,"Source"] = Source
    test_df.at[0,"Destination"] = Destination
    test_df.at[0,"Month_of_Journey"] = Month_of_Journey_Num
    test_df.at[0,"Day_of_Journey_Num"] = Day_of_Journey_Num
    test_df.at[0,"Distance"] = Distance
    test_df.at[0,"Stops_Counts"] = Stops_Counts
    test_df.at[0,"Dep_Hour"] = Dep_Hour
    test_df.at[0,"Categorized_Duration"] = Categorized_Duration
    test_df.at[0,"Meal"] = Meal
    test_df.at[0,"Arrival_Hour"] = Arrival_Hour
    test_df.at[0,"Arrival_Day_Period"] = Arrival_Day_Period
    test_df.at[0,"Dep_Day_Period"] = Dep_Day_Period
    result = Model.predict(test_df)
    return result[0]
def main():
    Airline = st.selectbox("Airline" ,['Air India', 'Jet Airways', 'IndiGo', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia'] )
    Source  = st.selectbox("Source" , ['Kolkata', 'Delhi', 'Banglore', 'Chennai', 'Mumbai'])
    Destination = st.selectbox("Destination" ,['Banglore', 'Cochin', 'New Delhi', 'Kolkata', 'Delhi', 'Hyderabad'] )
    Month_of_Journey_Num = st.selectbox("Month of Journey" ,[5, 6, 3, 4] )
    Stops_Counts = st.selectbox("Number of Stops" , [2, 1, 0, 3, 4])
    Day_of_Journey_Num = st.selectbox("Day of Journey" , [ 1,  9, 12, 24, 27, 18,  3, 15,  6, 21])
    Categorized_Duration = st.selectbox("Duration" , ['Short_duration', 'Medium_duration', 'Long_duration'])
    Distance = st.selectbox("Distance" , ['medium_distance', 'long_distance', 'short_distance'])
    Dep_Day_Period = st.selectbox("Departure Period" , ['Early_Morning', 'Afternoon', 'Evening', 'Night'])
    Arrival_Day_Period = st.selectbox("Arrival Period" ,['Afternoon', 'Night', 'Evening', 'Ealry_Morning'] )
    Dep_Hour = st.selectbox("Departure Hour",[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
    Arrival_Hour = st.selectbox("Arrival Hour",[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
    Meal = st.selectbox("Meal" , [0, 1])
    if st.button("predict"):
        results = prediction(Airline , Source , Destination , Month_of_Journey_Num , Day_of_Journey_Num , Distance , Stops_Counts , Dep_Hour , Categorized_Duration ,
               Meal , Arrival_Hour , Arrival_Day_Period , Dep_Day_Period)
        st.text(f"The flight cost will be {results}")
if __name__ == '__main__':
    main() 
