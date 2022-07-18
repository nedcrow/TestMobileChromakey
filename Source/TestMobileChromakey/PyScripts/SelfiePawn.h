// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Pawn.h"
#include "SelfiePawn.generated.h"

UCLASS()
class TESTMOBILECHROMAKEY_API ASelfiePawn : public APawn
{
	GENERATED_BODY()

public:
	ASelfiePawn();

public:
	UPROPERTY(BlueprintReadWrite, EditAnywhere)
	bool bCanURL = false;

};
