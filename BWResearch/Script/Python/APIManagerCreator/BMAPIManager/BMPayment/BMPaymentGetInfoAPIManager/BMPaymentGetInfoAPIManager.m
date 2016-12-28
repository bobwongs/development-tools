//
//  BMPaymentGetInfoAPIManager.m
//  BMWash
//
//  Created by BobWong on 16/12/17.
//  Copyright © 2016年 月亮小屋（中国）有限公司. All rights reserved.
//

#import "BMPaymentGetInfoAPIManager.h"

@implementation BMPaymentGetInfoAPIManager

- (NSString *)interfaceUrl
{
    return INTERFACE_PAYMENT_GET_INFO;
}

- (BOOL)useToken
{
    return YES;
}

@end
