//
//  BMServiceActivityGetProductList.m
//  BlueMoonHouse
//
//  Created by BobWong on 17/05/24.
//  Copyright © 2017年 月亮小屋（中国）有限公司. All rights reserved.

#import "BMServiceActivityGetProductList.h"

@implementation BMServiceActivityGetProductList

- (BOOL)isTestEnvironment
{
    return kBMIsTestEnvironment;
}

- (NSString *)formalApiBaseUrl
{
    return BASE_URL;
}

- (NSString *)testApiBasetUrl
{
#ifdef kISMockURL
    return BASE_URL_MOCK_TEST;
#else
    return BASE_URL_TEST;
#endif
}

- (NSString *)formalApiInterface
{
    return INTERFACE_ACTIVITY_GET_PRODUCT_LIST;
}

@end
