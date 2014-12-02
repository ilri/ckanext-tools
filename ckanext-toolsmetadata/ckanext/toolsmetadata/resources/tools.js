"use strict";

$("#tool_subjects").select2({ placeholder: "Select one or more subjects" });

$("#tool_themes").select2({ placeholder: "Select one or more themes" });

$("#tool_formats").select2({ placeholder: "Select one or more formats" });

$("#tool_datatypes").select2({ placeholder: "Select a data type" });

$("#tool_method").select2({ placeholder: "Select a method" });

$("#tool_audiance").select2({ placeholder: "Select an audiance" });

$("#tool_cycle").select2({ placeholder: "Select a stage" });

$("#tool_gender").select2({ placeholder: "Select a contribution" });

$("#tool_spscale").select2({ placeholder: "Select a spatial scale" });

$("#tool_orglevel").select2({ placeholder: "Select an organisational level" });

$("#tool_datasource").select2({ placeholder: "Select a data source" });

$("#tool_output").select2({ placeholder: "Select an output" });

$("#tool_assetype").select2({ placeholder: "Select a type of assessment" });

$(function()
{
  if (document.getElementById("SoftwareAccordion"))
  {
    $( "#SoftwareAccordion" ).accordion({collapsible: true, active: false });
  }

  if (document.getElementById("tool_lastupdate"))
  {
    $( "#tool_lastupdate" ).datepicker({ dateFormat: "dd/mm/yy", changeYear: true});
  }

  if (document.getElementById("datasettabs"))
  {
    $( "#datasettabs" ).tabs();
  }

});