#include "CppLib.h"
#include "Kismet/GameplayStatics.h"
#include "SelfiePawn.h"

#include "../Plugins/Experimental/PythonScriptPlugin/Source/PythonScriptPlugin/Private/PythonScriptPlugin.h"

void UCppLib::ExecutePythonScript(FString PythonScript) {
	FPythonScriptPlugin::Get()->ExecPythonCommand(*PythonScript);
}

void UCppLib::CanURL(FString URL)
{
	TArray<AActor*> actors;
	FString url;
	url.Append("s.can_url('");
	url.Append(URL);
	url.Append("')");
	FPythonScriptPlugin::Get()->ExecPythonCommand(*url);
}

void UCppLib::SetURL(bool canValue)
{
	UE_LOG(LogTemp, Warning, TEXT("connection is %s"), *FString(canValue ? "True" : "False"));
	TArray<AActor*> actors;
	if (GEditor != nullptr && GCurrentLevelEditingViewportClient != nullptr) {
		FWorldContext* world = GEngine->GetWorldContextFromGameViewport(GEngine->GameViewport);
		UGameplayStatics::GetAllActorsOfClassWithTag(world->World(), ASelfiePawn::StaticClass(), "SelfiePawn", actors);

		for (AActor* actor : actors)
		{
			ASelfiePawn* target = Cast<ASelfiePawn>(actor);
			target->bCanURL = canValue;
		}
	}
}
