// Copyright Epic Games, Inc. All Rights Reserved.

#include "MobileHelperBPLibrary.h"
#include "MobileHelper.h"

UMobileHelperBPLibrary::UMobileHelperBPLibrary(const FObjectInitializer& ObjectInitializer)
: Super(ObjectInitializer)
{

}

float UMobileHelperBPLibrary::MobileHelperSampleFunction(float Param)
{
	return -1;
}

void UMobileHelperBPLibrary::TestMessageFunction() {
	GEngine->AddOnScreenDebugMessage(-1, 5.f, FColor::Blue, TEXT("Test Message"));
}
