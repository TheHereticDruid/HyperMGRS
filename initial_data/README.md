### Initial Data
This directory has the initial data received from the governmental website and cleaned into csv formats. It also contains the original PDFs from which this data was received. Processing was done via a simple Python program, with conversion from PDF to CSV done via free online services.

Column information is as follows:
- **StuntedAssessmentParametersCleaned:** Assigned Sex (0 for Girl, 1 for Boy), Day count from birth, Height upper bound for severe stunting in cm, Height upper bound for moderate stunting in cm. (Each upper bound acts as the lower bound for the next class.)
- **UnderweightAssessmentParametersCleaned:** Assigned Sex (0 for Girl, 1 for Boy), Day count from birth, Weight upper bound for severely underweight in kg, Weight upper bound for moderately underweight in kg. (Each upper bound acts as the lower bound for the next class.)
- **WastedAssessmentParametersCleaned:** Assigned Sex (0 for Girl, 1 for Boy), Age slab (0 for 0-2 years, 1 for 2-5 years), Height in consideration in cm, Weight upper bound for severe acute malnutrition in kg, Weight upper bound for moderate acute malnutrition in kg, Weight upper bound for normal weight in kg, Weight upper bound for above normal weight in kg. (Each upper bound acts as the lower bound for the next class.)

Classes in consideration for each metric:
- **Stunting (StuntedAssessmentParametersCleaned):** Severe Stunting, Moderate Stunting, Normal
- **Underweight (UnderweightAssessmentParametersCleaned):** Severely Underweight, Moderately Underweight, Normal
- **Wasting (WastedAssessmentParametersCleaned):** Severe Acute Malnutrition, Moderate Acute Malnutrition, Normal, Overweight, Obese