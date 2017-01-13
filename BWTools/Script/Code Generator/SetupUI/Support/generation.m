Getter:
- (BMAppointmentDetailSingleRowView *)viewOrder {
   if (!_viewOrder) {
      _viewOrder = [BMAppointmentDetailSingleRowView <#Method#>];
   }
   return _viewOrder;
}

- (BMAppointmentDetailSingleRowView *)viewTime {
   if (!_viewTime) {
      _viewTime = [BMAppointmentDetailSingleRowView <#Method#>];
   }
   return _viewTime;
}

- (BMAppointmentDetailMultilineView *)viewWashCenter {
   if (!_viewWashCenter) {
      _viewWashCenter = [BMAppointmentDetailMultilineView <#Method#>];
   }
   return _viewWashCenter;
}



setUI:
_viewOrder = [BMAppointmentDetailSingleRowView <#Method#>];
_viewTime = [BMAppointmentDetailSingleRowView <#Method#>];
_viewWashCenter = [BMAppointmentDetailMultilineView <#Method#>];

[<#view#> addSubview:_viewOrder];
[<#view#> addSubview:_viewTime];
[<#view#> addSubview:_viewWashCenter];


Masonry:
[_viewOrder mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_viewTime mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_viewWashCenter mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

