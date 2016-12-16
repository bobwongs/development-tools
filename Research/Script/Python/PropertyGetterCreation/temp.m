Getter:
- (UIScrollView *)scrollView {
   if (!_scrollView) {
      _scrollView = [UIScrollView <#Method#>];
   }
   return _scrollView;
}

- (UIButton *)btnSelectAddress {
   if (!_btnSelectAddress) {
      _btnSelectAddress = [UIButton <#Method#>];
   }
   return _btnSelectAddress;
}

- (UIImageView *)ivLocationIcon {
   if (!_ivLocationIcon) {
      _ivLocationIcon = [UIImageView <#Method#>];
   }
   return _ivLocationIcon;
}

- (UILabel *)lbLocation {
   if (!_lbLocation) {
      _lbLocation = [UILabel <#Method#>];
   }
   return _lbLocation;
}

- (UIImageView *)ivArrow {
   if (!_ivArrow) {
      _ivArrow = [UIImageView <#Method#>];
   }
   return _ivArrow;
}

- (UIView *)viewMiddle {
   if (!_viewMiddle) {
      _viewMiddle = [UIView <#Method#>];
   }
   return _viewMiddle;
}

- (UILabel *)lbGetClothesWayDesc {
   if (!_lbGetClothesWayDesc) {
      _lbGetClothesWayDesc = [UILabel <#Method#>];
   }
   return _lbGetClothesWayDesc;
}

- (UIButton *)btnGetClothesVisit {
   if (!_btnGetClothesVisit) {
      _btnGetClothesVisit = [UIButton <#Method#>];
   }
   return _btnGetClothesVisit;
}

- (UIButton *)btnGetClothesExpress {
   if (!_btnGetClothesExpress) {
      _btnGetClothesExpress = [UIButton <#Method#>];
   }
   return _btnGetClothesExpress;
}

- (UIView *)viewGetClothesMsg {
   if (!_viewGetClothesMsg) {
      _viewGetClothesMsg = [UIView <#Method#>];
   }
   return _viewGetClothesMsg;
}

- (UILabel *)lbFeeDesc {
   if (!_lbFeeDesc) {
      _lbFeeDesc = [UILabel <#Method#>];
   }
   return _lbFeeDesc;
}

- (UILabel *)lbFee {
   if (!_lbFee) {
      _lbFee = [UILabel <#Method#>];
   }
   return _lbFee;
}

- (UILabel *)lbSendTip0 {
   if (!_lbSendTip0) {
      _lbSendTip0 = [UILabel <#Method#>];
   }
   return _lbSendTip0;
}

- (UILabel *)lbSendTargetPerson {
   if (!_lbSendTargetPerson) {
      _lbSendTargetPerson = [UILabel <#Method#>];
   }
   return _lbSendTargetPerson;
}

- (UILabel *)lbSendTargetLocation {
   if (!_lbSendTargetLocation) {
      _lbSendTargetLocation = [UILabel <#Method#>];
   }
   return _lbSendTargetLocation;
}

- (UILabel *)lbRemarkDesc {
   if (!_lbRemarkDesc) {
      _lbRemarkDesc = [UILabel <#Method#>];
   }
   return _lbRemarkDesc;
}

- (UILabel *)lbRemark {
   if (!_lbRemark) {
      _lbRemark = [UILabel <#Method#>];
   }
   return _lbRemark;
}

- (UIButton *)btnConfirm {
   if (!_btnConfirm) {
      _btnConfirm = [UIButton <#Method#>];
   }
   return _btnConfirm;
}



  setUI:
_scrollView = [UIScrollView <#Method#>];
_btnSelectAddress = [UIButton <#Method#>];
_ivLocationIcon = [UIImageView <#Method#>];
_lbLocation = [UILabel <#Method#>];
_ivArrow = [UIImageView <#Method#>];
_viewMiddle = [UIView <#Method#>];
_lbGetClothesWayDesc = [UILabel <#Method#>];
_btnGetClothesVisit = [UIButton <#Method#>];
_btnGetClothesExpress = [UIButton <#Method#>];
_viewGetClothesMsg = [UIView <#Method#>];
_lbFeeDesc = [UILabel <#Method#>];
_lbFee = [UILabel <#Method#>];
_lbSendTip0 = [UILabel <#Method#>];
_lbSendTargetPerson = [UILabel <#Method#>];
_lbSendTargetLocation = [UILabel <#Method#>];
_lbRemarkDesc = [UILabel <#Method#>];
_lbRemark = [UILabel <#Method#>];
_btnConfirm = [UIButton <#Method#>];

[<#view#> addSubview:_scrollView];
[<#view#> addSubview:_btnSelectAddress];
[<#view#> addSubview:_ivLocationIcon];
[<#view#> addSubview:_lbLocation];
[<#view#> addSubview:_ivArrow];
[<#view#> addSubview:_viewMiddle];
[<#view#> addSubview:_lbGetClothesWayDesc];
[<#view#> addSubview:_btnGetClothesVisit];
[<#view#> addSubview:_btnGetClothesExpress];
[<#view#> addSubview:_viewGetClothesMsg];
[<#view#> addSubview:_lbFeeDesc];
[<#view#> addSubview:_lbFee];
[<#view#> addSubview:_lbSendTip0];
[<#view#> addSubview:_lbSendTargetPerson];
[<#view#> addSubview:_lbSendTargetLocation];
[<#view#> addSubview:_lbRemarkDesc];
[<#view#> addSubview:_lbRemark];
[<#view#> addSubview:_btnConfirm];


  Masonry:
[_scrollView mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_btnSelectAddress mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_ivLocationIcon mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_lbLocation mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_ivArrow mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_viewMiddle mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_lbGetClothesWayDesc mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_btnGetClothesVisit mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_btnGetClothesExpress mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_viewGetClothesMsg mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_lbFeeDesc mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_lbFee mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_lbSendTip0 mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_lbSendTargetPerson mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_lbSendTargetLocation mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_lbRemarkDesc mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_lbRemark mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_btnConfirm mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

