//
//  BMMoonTicketQueryRemainAPIManager.m
//  BMWash
//
//  Created by BobWong on 16/12/17.
//  Copyright © 2016年 月亮小屋（中国）有限公司. All rights reserved.
//

#import "BMMoonTicketQueryRemainAPIManager.h"

@implementation BMMoonTicketQueryRemainAPIManager

- (NSString *)interfaceUrl
{
    return INTERFACE_MOON_TICKET_QUERY_REMAIN;
}

- (BOOL)useToken
{
    return YES;
}

@end
