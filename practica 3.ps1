function iniciar_sesion{
  param
  (
    [Parameter(Mandatory=$true, ValueFromPipeline=$true)]
    [String[]]
    [AllowEmptyString()] 
    $User,$Pass
  )
 
    Write-Host "Principio de login"
    $usercorrecto="Ramon"
    $passcorrecto="P4ssW0rd"
 
   if($User -eq $usercorrecto -and $Pass -eq $passcorrecto){
        $ok=1
    }else{
        $ok=0
    }

   if($ok){
        Write-Host "User correcto"
    }else{
        if($User -ne $usercorrecto){
            Write-Host "usuario incorrecto"
        }else{
            Write-Host "contraseña incorrecta"
        }
    }
    Write-Host "Fin de login"
    Write-Host ""
}
 
iniciar_sesion Ramon Contraseña
iniciar_sesion Romon p4ssw0rd
iniciar_sesion Ramon p4ssw0rd