let select = ""
  let num=""
  
  let num2=""
        let url = 'https://apis.digital.gob.cl/dpa/regiones';
        fetch(url)
              .then( response => response.json() )
              .then( data => {
                console.log(data)
              
              for (var i = 0; i < data.length; i++) {
                if (i==0)  {
                  select += '<option value="' + data[i].codigo + '"'+ ' selected disabled' +'>' + '--Region--' + '</option>'
                 num+=(data[i].codigo )
                }
                select += '<option value="' + data[i].codigo + '">' + data[i].nombre + '</option>'
                 num+=(data[i].codigo)
                 
              }
  
              document.getElementById('region').innerHTML = select
              console.log(select)
             
              })
              .catch( error => console.log(error) )
  
              $('#region').change(function() {
                var codigo= $('#region').val();
                  let url2 = `https://apis.digital.gob.cl/dpa/regiones/${codigo}/comunas`;
              fetch(url2)
                    .then( response2 => response2.json() )
                    .then( data2 => {
                      console.log(data2)
                      let select2 = "";
                    for (var i = 0; i < data2.length; i++) {
                      if (i==0)  {
                        select2 += '<option value="' + data2[i].codigo + '"'+ ' selected disabled' +'>' + '--Comuna--' + '</option>'
                      num2+=(data2[i].codigo )
                      }
                      select2 += '<option>' + data2[i].nombre + '</option>'
                       num2+=(data2[i].codigo)  
                    }
        
                    document.getElementById('comuna').innerHTML = select2
                    console.log(select2)
                   
                    })
                    .catch( error => console.log(error) )
              });
              
              setTimeout(function() {$('#region').trigger('change');}, 2000);