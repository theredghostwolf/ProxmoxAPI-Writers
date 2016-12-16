###python scripts for writing REST points for the proxmox api / writing the api its self

usage:

writeProxmoxApi.py:

  create inputfile in the format:
    
    proxmox api link /nodes/{node}/qemu/{qemu}/status
    http.method       GET
                      POST
                      
    this creates a get and post method for the given link
    
    python writeProxmoxApi.py input.txt output.txt
    
    
writeNodeApi:
  
  create inputfile in the format:
      
     functionname (function parameters) qemu.getStatus (node, vmid, callback);
     
   this creates a node js method for calling this function from angular
   
   python writeNodeApi.py input.txt > output.txt
 
 
 
 writeAngularApi:
 
   create inputfile in the format:
      
     functionname (function parameters) qemu.getStatus (node, vmid, callback);
     
    this creates a $scope.functionname function so you can call the node JS rest point
    
    python writeAngularApi.py input.txt output.txt
