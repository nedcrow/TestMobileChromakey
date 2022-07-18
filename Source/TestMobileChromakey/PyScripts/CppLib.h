
#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "CppLib.generated.h"

/**
 * 
 */
UCLASS()
class TESTMOBILECHROMAKEY_API UCppLib : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	
public:
	UFUNCTION(BlueprintCallable, Category = "UEPython")
		static void ExecutePythonScript(FString PythonScript);

	UFUNCTION(BlueprintCallable, Category = "UEPython")
		static void CanURL(FString URL);

	UFUNCTION(BlueprintCallable, Category = "UEPython")
		static void SetURL(bool canValue);
};
