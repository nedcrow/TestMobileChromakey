// Fill out your copyright notice in the Description page of Project Settings.


#include "VirtualCameraComponent.h"

// Sets default values for this component's properties
UVirtualCameraComponent::UVirtualCameraComponent()
{
	// Set this component to be initialized when the game starts, and to be ticked every frame.  You can turn these features
	// off to improve performance if you don't need them.
	PrimaryComponentTick.bCanEverTick = true;

	// ...
}


// Called when the game starts
void UVirtualCameraComponent::BeginPlay()
{
	Super::BeginPlay();

	FHttpModule * Http = &FHttpModule::Get();
	FHttpRequestRef RequestRef = Http->CreateRequest();
	RequestRef->OnProcessRequestComplete().BindUObject(this, &UVirtualCameraComponent::OnResRecived);
	//RequestRef->SetURL("https://jsonplaceholder.typicode.com/posts/1");
	RequestRef->SetURL("http://192.168.1.179:3000");
	RequestRef->SetVerb("Get");
	RequestRef->ProcessRequest();

	UE_LOG(LogTemp, Warning, TEXT("Huhuhu"));
	// ...
	
}


void UVirtualCameraComponent::OnResRecived(FHttpRequestPtr Req, FHttpResponsePtr Res, bool Successfully)
{
	UE_LOG(LogTemp, Warning, TEXT("OnResRecived"));
}

