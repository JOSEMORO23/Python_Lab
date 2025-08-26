package com.jwt.jwt_auth.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.jwt.jwt_auth.JwtUtil;
import com.jwt.jwt_auth.dao.UsuarioRepository;

@Service
public class AuthService {

    @Autowired
    private UsuarioRepository usuarioRepository;

    @Autowired
    private JwtUtil jwtUtil;

    public String login(String username, String password) {
        return usuarioRepository.findByUsername(username)
                .filter(user -> user.getPassword().equals(password))
                .map(user -> jwtUtil.generateToken(user.getUsername()))
                .orElseThrow(() -> new RuntimeException("Credenciales inválidas"));
    }
}

