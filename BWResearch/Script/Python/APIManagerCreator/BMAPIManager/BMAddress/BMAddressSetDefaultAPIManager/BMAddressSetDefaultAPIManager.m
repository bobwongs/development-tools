//
//  BMAddressSetDefaultAPIManager.m
//  BMWash
//
//  Created by BobWong on 16/12/17.
//  Copyright © 2016年 月亮小屋（中国）有限公司. All rights reserved.
//

#import "BMAddressSetDefaultAPIManager.h"

@implementation BMAddressSetDefaultAPIManager

- (NSString *)interfaceUrl
{
    return INTERFACE_ADDRESS_SET_DEFAULT;
}

- (BOOL)useToken
{
    return YES;
}

@end
