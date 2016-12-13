Getter:
- (UIImageView *)ivTop {
   if (!_ivTop) {
      _ivTop = [UIImageView <#Method#>];
   }
   return _ivTop;
}

- (UILabel *)lbPaySuccess {
   if (!_lbPaySuccess) {
      _lbPaySuccess = [UILabel <#Method#>];
   }
   return _lbPaySuccess;
}

- (UILabel *)lbThanks {
   if (!_lbThanks) {
      _lbThanks = [UILabel <#Method#>];
   }
   return _lbThanks;
}

- (UIButton *)btnContinue {
   if (!_btnContinue) {
      _btnContinue = [UIButton <#Method#>];
   }
   return _btnContinue;
}

- (UIButton *)btnSeeOrder {
   if (!_btnSeeOrder) {
      _btnSeeOrder = [UIButton <#Method#>];
   }
   return _btnSeeOrder;
}



  setUI:
_ivTop = [UIImageView <#Method#>];
_lbPaySuccess = [UILabel <#Method#>];
_lbThanks = [UILabel <#Method#>];
_btnContinue = [UIButton <#Method#>];
_btnSeeOrder = [UIButton <#Method#>];

[<#view#> addSubview:_ivTop];
[<#view#> addSubview:_lbPaySuccess];
[<#view#> addSubview:_lbThanks];
[<#view#> addSubview:_btnContinue];
[<#view#> addSubview:_btnSeeOrder];


  Masonry:
[_ivTop mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_lbPaySuccess mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_lbThanks mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_btnContinue mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];

[_btnSeeOrder mas_makeConstraints:^(MASConstraintMaker *make) {
    make.left.mas_equalTo(<#CGFloat#>);
    make.right.mas_equalTo(<#CGFloat#>);
    make.top.mas_equalTo(<#CGFloat#>);
    make.bottom.mas_equalTo(<#CGFloat#>);
}];



