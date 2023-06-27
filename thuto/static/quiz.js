function getAnswers()
{
  document.getElementById(UserAnswers).innerHTML="";
  var e=document.getElementsByName("input");
  for(i=0,i<=e.length; i++;)
  {
    if(e[i].type=="radio")
    {
      if(e[i].checked)
      {
        document.getElementById(UserAnswers).innerHTML+="Q "+e[i].name+"the answer you selected is :"+e[i].value+"<br/>";
      }
    }
  }
}

$(document).ready(function(){
  $("#but1").click(function(){
    $(".rb").show();
    $(".rb").attr("disabled",true);

  });

}
);