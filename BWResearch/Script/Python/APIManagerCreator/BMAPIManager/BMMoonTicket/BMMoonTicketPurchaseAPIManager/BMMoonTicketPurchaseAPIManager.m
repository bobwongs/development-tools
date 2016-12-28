//
//  BMMoonTicketPurchaseAPIManager.m
//  BMWash
//
//  Created by BobWong on 16/12/17.
//  Copyright © 2016年 月亮小屋（中国）有限公司. All rights reserved.
//

#import "BMMoonTicketPurchaseAPIManager.h"

@implementation BMMoonTicketPurchaseAPIManager

- (NSString *)interfaceUrl
{
    return INTERFACE_MOON_TICKET_PURCHASE;
}

- (BOOL)useToken
{
    return YES;
}

@end
