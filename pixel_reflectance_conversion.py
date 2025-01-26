import os
import arcpy # type: ignore
from arcpy.sa import * # type: ignore

arcpy.CheckOutExtension("Spatial")

TOA_input = "D:\\Digital_Image\\practice\\TOA_input"
TOA_output = "D:\\Digital_Image\\practice\\toa_output"

scale_factor = 0.0000275
offset_value = -0.2

for file_name in os.listdir(TOA_input):
    if file_name.endswith(".TIF"): 
        input_raster = os.path.join(TOA_input, file_name)
        output_raster = os.path.join(TOA_output, f"Reflectance_{file_name}")
        
        # Print the output path to verify
        print(f"Output raster will be saved to: {output_raster}")
        
        formula = f"({scale_factor} * Raster('{input_raster}')) + {offset_value}"
        
        try:
            arcpy.gp.RasterCalculator_sa(formula, output_raster)
            print(f"Processed {file_name} -> Saved as {output_raster}")
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

# Print output folder contents to verify
print("Contents of output folder:", os.listdir(TOA_output))

arcpy.CheckInExtension("Spatial")

print("All TIF files processed successfully!")
